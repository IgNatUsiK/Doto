# Boot by IgNatUsiK
# Created at 07.03.2022 11:35

# Booting
try:
	# Loading config
	exec(open("syscnf.ini", "r", encoding="utf-8").read())
	print("Config loaded...")
	exec(open(f"System/Lang/{lang}.lang", "r", encoding="utf-8").read())
	print("Language loaded...")

	# Start
	exec(open(bootStart, "r", encoding="utf-8").read())
	# Main
	exec(open(bootMain, "r", encoding="utf-8").read())
	# Stop
	exec(open(bootStop, "r", encoding="utf-8").read())

	# Normal end
	print("[Successful finish]")

# Except for error
except BaseException as error:
	# Fatal
	print("Fatal error :(\nDoto stopped due to fatal error\nError:", error)

	# End with error
	print("[Bad finish]")