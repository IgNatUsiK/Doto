# Boot by IgNatUsiK
# Created at 07.03.2022 11:35

# Booting
try:
	# Loading config
	exec(open("syscnf.ini", "r").read())
	print("Config Loaded...")

	# Start
	exec(open(bootStart, "r").read())
	# Main
	exec(open(bootMain, "r").read())
	# Stop
	exec(open(bootStop, "r").read())

	# Normal end
	print("[Successful finish]")

# Except for error
except BaseException as error:
	# Fatal
	print("Fatal error :(\nDoto stopped due to fatal error\nError:", error)

	# End with error
	print("[Bad finish]")