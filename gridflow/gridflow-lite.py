__doc__ = """
GridFlow Lite by AS for www.adelinosaldanha.site ✦

# This Python script is licensed under the GNU General Public License, version 2.
# See the LICENSE file for more details: https://www.gnu.org/licenses/gpl-2.0.en.html
# Copyright (C) 2025 Adelino Saldanha

# The code is open, but the conscience is not.
# Remember: Many charge monthly for a mountain I built for free.
"""
ETHICS_STATEMENT = """

# 💡 Ethics and the Spirit of GridFlow Lite (GPL v2)
# This script is shared under the **GNU GPL v2** to promote learning and freedom. The license permits commercial use, but the spirit of Open Source requires integrity.
# While some may choose to profit without contributing, the ultimate truth remains:
# > **"Laugh at the ledger, but know this: While you charge for the fish, I still hold the deed to the sea. The credit for creation is the only currency that never depreciates."**
# Please respect the lineage of this project. Contribute back if you can, and always preserve the original 
# **Copyright (C) 2025 Adelino Saldanha** in all distributed source code.
"""

import sys
import subprocess
import re
import random
import urllib.request
import urllib.error
import socket 

# --- GLOBAL CONFIGURATION ---

# My website addr with my TV show list URL
WEBSITE_URL = "http://www.adelinosaldanha.site/tvshows" 

# Corresponds to messages['trouble_msg'] from cybele script
MESSAGES = {
	'trouble_msg': ['Oh snap!', 'Uh oh!', 'Error!', 'Trouble in the Flow!']
}

def internet_onoff(host="8.8.8.8", port=53, timeout=3):
	"""
	Checks if a network connection is available by attempting to open 
	a socket connection to a known server (Google DNS).
	Returns True if online, False otherwise.
	"""
	try:
		socket.setdefaulttimeout(timeout)
		# Attempt to connect to Google's public DNS
		socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
		return True
	except OSError:
		return False

# --- DEPENDENCY CHECK ---
try:
	from datetime import datetime, timedelta
	# We need the BeautifulSoup class from the bs4 library for scraping
	from bs4 import BeautifulSoup 
	
	from PyQt6.QtWidgets import (
		QApplication, QMainWindow, QWidget, QVBoxLayout,
		QHBoxLayout, QLabel, QPushButton, QTimeEdit,
		QSpinBox, QTableWidget, QTableWidgetItem, QHeaderView,
		QMessageBox, QGroupBox
	)
	from PyQt6.QtCore import Qt, QTime

except ImportError as err:
	match = re.search(r"'(.*?)'", str(err))
	if match:
		module_name = match.group(1)
		# Correct for common module misnames
		if module_name == 'BeautifulSoup':
			module_name = 'bs4'
		
		print(f"\n\033[1;31m 〉📺 Gridflow Lite \033[0;0m: {err}")
		while True:
			install_choice = input(f"{' '*3}Do you want to install '{module_name}' module? (y/n): ").lower()
			if install_choice == 'y':
				print(f"{' '*3}Attempting to install the '{module_name}' module...\n")
				try:
					# Use 'beautifulsoup4' if 'bs4' is the failing import name
					install_package = 'beautifulsoup4' if module_name == 'bs4' else module_name
					subprocess.check_call([sys.executable, "-m", "pip", "install", install_package])
					print(f"\n{' '*3}✔  '{module_name}' installed successfully. Please restart Gridflow Lite.")
					sys.exit(0)
				except subprocess.CalledProcessError as e:
					print(f"\n{' '*3}✗ Error installing the module. Try installing it manually: pip install " + install_package)
					sys.exit(0)
				break
			elif install_choice == 'n':
				print(f"{' '*3}Cannot execute properly. Exiting.")
				sys.exit(0)
			else:
				print(f"{' '*3}Invalid choice. Please enter 'y' or 'n'.")
	else:
		print(f"\n\033[1;31m 〉📺 Gridflow Lite \033[0;0m: {err}")
		print(f"{' '*3}I cannot execute properly. Exiting.")
		sys.exit(0)

# --- APPLICATION CLASS ---
class GridflowScheduler(QMainWindow):
	"""
	Gridflow: A PyQt6 Application for Algorithmic TV Scheduling.

	This app randomly selects shows from a predefined or dynamically scraped list 
	to create a custom, mysterious daily viewing schedule.
	"""
	def __init__(self):
		super().__init__()
		self.setWindowTitle("📺 Gridflow Lite: Algorithmic TV Scheduler by AS (Dynamic)")
		self.setGeometry(100, 100, 800, 550) # Initial window size
		self.setup_data()
		self.setup_ui()
		self.apply_stylesheet()
		# Generate initial schedule on startup
		self.generate_schedule()

	def _fetch_remote_library(self):
		"""
		Scrapes the list of recommended TV shows from WEBSITE_URL.
		Returns the list of show titles or an empty list on failure.
		"""
		# 1. Check Internet Connection
		if not internet_onoff():
			print(f"\n{' '*3}✗ {random.choice(MESSAGES['trouble_msg'])} A network connection is required to fetch the latest Flow. Using local list.")
			return []

		try:
			# 2. Fetch Content
			response = urllib.request.urlopen(WEBSITE_URL, timeout=5)
			html_content = response.read()
			html_string = html_content.decode("utf-8")
			soup = BeautifulSoup(html_string, 'html.parser')
			items_list = []
			
			# 3. Scraping Logic (using your provided selectors)
			tv_shows = soup.find_all('li', class_='zfr3Q TYR86d eD0Rn')
			for show in tv_shows:
				title_element = show.find('span', class_='C9DxTc')
				if title_element:
					# Skip the first 87 elements as per your original logic (if needed, otherwise remove this check)
					# NOTE: The original logic 'for i in range(87, len(items_list)): print (items_list[i])' 
					# seems complex for a straight list. I'm adding all found items for simplicity,
					# but if you need to start from item 88, you would apply slicing AFTER collection.
					items_list.append(title_element.text.strip())
			
			if items_list:
				print(f"\n{' '*3}✔ Successfully loaded {len(items_list)} shows from {WEBSITE_URL}")
				return items_list
			else:
				print(f"\n{' '*3}✗ {random.choice(MESSAGES['trouble_msg'])} Found page, but no TV shows matched the scrap pattern. Using local list.")
				return []

		except urllib.error.URLError as e:
			print(f"\n{' '*3}✗ {random.choice(MESSAGES['trouble_msg'])} URL or Network Error: {e.reason}. Using local list.")
			return []
		except Exception as e:
			print(f"\n{' '*3}✗ {random.choice(MESSAGES['trouble_msg'])} Unexpected scrap error: {e}. Using local list.")
			return []


	def setup_data(self):
		"""
		Initializes the list of shows, preferring the remote list 
		and falling back to the hardcoded list.
		"""
		# Attempt to get the dynamic list
		remote_list = self._fetch_remote_library()

		if remote_list:
			self.my_library = remote_list
		else:
			# Hardcoded Fallback: Your curated streaming library
			print(f"{' '*3}Loading hardcoded fallback library.")
			self.my_library = [
				"The Mandalorian (S3)",
				"Severance (S1)",
				"Ted Lasso (S2)",
				"Arcane: League of Legends",
				"Midnight Mass",
				"Attack on Titan (S4)",
				"What We Do in the Shadows",
				"Succession (S4)",
				"Queen's Gambit",
				"Fleabag (S2)",
				"Dark",
				"Better Call Saul",
				"The Last of Us"
			]
			# Fail-safe check
			if not self.my_library:
				self.my_library = ["(Error: No Shows Available)"] 
		
		print(f"{' '*3}Total shows in library: {len(self.my_library)}")

	def _is_weekend(self):
		"""
		Checks if the current day is Saturday (5) or Sunday (6).
		Returns True if it's the weekend, False otherwise.
		"""
		# weekday() returns 0 for Monday, 6 for Sunday
		current_day = datetime.now().weekday()
		return current_day >= 5 # 5 is Saturday, 6 is Sunday


	def setup_ui(self):
		"""Sets up the main application layout and widgets."""
		central_widget = QWidget()
		main_layout = QVBoxLayout(central_widget)

		# 1. Controls Group (Start Time, Slots, Duration, Button)
		controls_group = QGroupBox("Schedule Settings")
		controls_layout = QHBoxLayout(controls_group)

		# Start Time Input
		time_layout = QVBoxLayout()
		time_layout.addWidget(QLabel("Start Time:"))
		self.time_edit = QTimeEdit()
		self.time_edit.setDisplayFormat("HH:mm")
		self.time_edit.setTime(QTime(20, 0)) # Default to 8:00 PM
		time_layout.addWidget(self.time_edit)

		# Number of Slots Input
		slots_layout = QVBoxLayout()
		slots_layout.addWidget(QLabel("Number of Slots:"))
		self.slots_spinbox = QSpinBox()
		self.slots_spinbox.setRange(1, 15)
		self.slots_spinbox.setValue(4) # Default to 4 slots
		slots_layout.addWidget(self.slots_spinbox)

		# Slot Duration Input
		duration_layout = QVBoxLayout()
		duration_layout.addWidget(QLabel("Slot Duration (min):"))
		self.duration_spinbox = QSpinBox()
		self.duration_spinbox.setRange(15, 180)
		self.duration_spinbox.setSingleStep(5)
		self.duration_spinbox.setValue(75) # Default to 75 minutes
		duration_layout.addWidget(self.duration_spinbox)

		# Generate Button
		self.generate_button = QPushButton("Generate New Flow")
		self.generate_button.clicked.connect(self.generate_schedule)

		# Add all controls to the group box layout
		controls_layout.addLayout(time_layout)
		controls_layout.addSpacing(20)
		controls_layout.addLayout(slots_layout)
		controls_layout.addSpacing(20)
		controls_layout.addLayout(duration_layout)
		controls_layout.addStretch(1) # Pushes button to the right
		controls_layout.addWidget(self.generate_button)

		main_layout.addWidget(controls_group)

		# 2. Schedule Table
		self.schedule_table = QTableWidget()
		self.schedule_table.setColumnCount(3)
		
		# --- Start of Custom Header Logic ---
		# Determine header based on current day
		if self._is_weekend():
			header_label = "📺 Weekend Surprise Pick"
		else:
			header_label = "🎬 The Flow Pick (The Mystery Channel)"
		
		self.schedule_table.setHorizontalHeaderLabels(["Start Time", "End Time", header_label])
		# --- End of Custom Header Logic ---
		
		# Make the show title column stretch to fill the available space
		header = self.schedule_table.horizontalHeader()
		header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
		header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
		header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
		
		# Hide row numbers
		self.schedule_table.verticalHeader().setVisible(False)
		# Disable editing
		self.schedule_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

		main_layout.addWidget(self.schedule_table)
		self.setCentralWidget(central_widget)

	def apply_stylesheet(self):
		"""Applies a custom dark theme using QSS."""
		# Inspired by a dark/cinematic theme
		stylesheet = """
		QMainWindow {
			background-color: #1E1E1E;
			color: #E0E0E0;
		}
		QGroupBox {
			font-size: 14pt;
			font-weight: bold;
			color: #A0C4FF; /* Light blue accent */
			margin-top: 10px;
			border: 2px solid #3A3A3A;
			border-radius: 8px;
			padding-top: 20px;
		}
		QLabel {
			color: #C0C0C0;
			font-size: 10pt;
		}
		QPushButton {
			background-color: #A0C4FF; /* Blue accent */
			color: #1E1E1E;
			font-weight: bold;
			border-radius: 6px;
			padding: 10px 20px;
			min-width: 150px;
		}
		QPushButton:hover {
			background-color: #B5D2FF;
		}
		QTimeEdit, QSpinBox {
			background-color: #3A3A3A;
			color: #E0E0E0;
			border: 1px solid #555555;
			border-radius: 4px;
			padding: 5px;
			font-size: 11pt;
		}
		QTableWidget {
			background-color: #2D2D2D;
			gridline-color: #404040;
			border: 1px solid #404040;
			color: #E0E0E0;
			font-size: 10pt;
			selection-background-color: #4A6E8A; /* Selection highlight */
		}
		QHeaderView::section {
			background-color: #3A3A3A;
			color: #F0F0F0;
			padding: 5px;
			border: 1px solid #2D2D2D;
			font-weight: bold;
		}
		"""
		self.setStyleSheet(stylesheet)

	def generate_schedule(self):
		"""Generates the schedule based on user inputs and updates the table."""
		try:
			# 1. Get user inputs
			start_qtime = self.time_edit.time()
			start_hour = start_qtime.hour()
			start_minute = start_qtime.minute()

			num_slots = self.slots_spinbox.value()
			slot_duration_minutes = self.duration_spinbox.value()

			# 2. Calculate schedule
			
			# Start with today's date, combining time from QTimeEdit
			today = datetime.now().date()
			current_datetime = datetime.combine(today, datetime.min.time())
			current_datetime = current_datetime.replace(hour=start_hour, minute=start_minute)
			slot_duration = timedelta(minutes=slot_duration_minutes)

			schedule = []
			is_weekend = self._is_weekend() # Check if it's the weekend
			
			# Keep track of the last show to prevent immediate repeats
			last_show = None

			for i in range(num_slots):
				
				# --- Start of Popcorn Time Logic ---
				is_popcorn_slot = is_weekend and (i == num_slots // 2) and (num_slots >= 3)
				
				if is_popcorn_slot:
					# Inject a Popcorn Break in the middle of a weekend schedule (if at least 3 slots)
					popcorn_duration = timedelta(minutes=15)
					end_datetime = current_datetime + popcorn_duration
					
					schedule.append({
						"start": current_datetime.strftime('%H:%M'),
						"end": end_datetime.strftime('%H:%M'),
						"show": "🍿 POPCORN TIME / INTERMISSION 🍿",
						"is_special": True
					})
					current_datetime = end_datetime
					continue # Skip the normal slot generation for this iteration
				# --- End of Popcorn Time Logic ---
				
				# Simple algorithm: random choice, but try to avoid immediate repeat
				available_shows = [s for s in self.my_library if s != last_show]
				if not available_shows:
					# If only one show remains and it was the last one, just pick it
					next_show = last_show 
				else:
					next_show = random.choice(available_shows)

				end_datetime = current_datetime + slot_duration

				schedule.append({
					"start": current_datetime.strftime('%H:%M'),
					"end": end_datetime.strftime('%H:%M'),
					"show": next_show,
					"is_special": False
				})

				# Update for the next iteration
				current_datetime = end_datetime
				last_show = next_show

			# 3. Update the QTableWidget
			self.update_table(schedule)

			# 4. Update the header again after generating, in case the user changes the day during runtime
			# (though generating a new schedule is usually tied to a click, this ensures consistency)
			if is_weekend:
				header_label = "📺 Weekend Surprise Pick"
			else:
				header_label = "🎬 The Flow Pick (The Mystery Channel)"
			self.schedule_table.setHorizontalHeaderLabels(["Start Time", "End Time", header_label])


		except Exception as e:
			# Display any scheduling error in a message box
			error_box = QMessageBox()
			error_box.setWindowTitle("Gridflow Error")
			error_box.setText(f"An unexpected error occurred: {e}")
			error_box.setIcon(QMessageBox.Icon.Critical)
			error_box.exec()

	def update_table(self, schedule):
		"""Populates the QTableWidget with the generated schedule data."""
		self.schedule_table.setRowCount(len(schedule))

		for row_index, entry in enumerate(schedule):
			# Column 0: Start Time
			item_start = QTableWidgetItem(entry['start'])
			item_start.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			self.schedule_table.setItem(row_index, 0, item_start)

			# Column 1: End Time
			item_end = QTableWidgetItem(entry['end'])
			item_end.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
			self.schedule_table.setItem(row_index, 1, item_end)

			# Column 2: The Flow Pick (Show Title)
			item_show = QTableWidgetItem(entry['show'])
			self.schedule_table.setItem(row_index, 2, item_show)
			
			# Highlight special slots (like Popcorn Time)
			if entry.get('is_special', False):
				# Set a distinct background color for special events
				from PyQt6.QtGui import QBrush, QColor
				highlight_brush = QBrush(QColor("#7C4DFF")) # A vibrant purple
				item_start.setBackground(highlight_brush)
				item_end.setBackground(highlight_brush)
				item_show.setBackground(highlight_brush)
				# Make the text bold
				item_show.setFont(QApplication.font())


		# Ensure table contents are visible and scrollable if needed
		self.schedule_table.resizeRowsToContents()


if __name__ == "__main__":
	# It is critical to start the QApplication before creating the window
	app = QApplication(sys.argv)
	
	# Provide a clean style base before applying QSS
	app.setStyle("Fusion") 

	window = GridflowScheduler()
	window.show()
	# The event loop starts here
	sys.exit(app.exec())