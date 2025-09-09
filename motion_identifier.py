# Motion Type Identifier

# Function 1: Convert velocity to m/s
def convert_velocity(value, unit):
    """
    Convert velocity to meters per second (m/s)
    Supported units: m/s, ft/s, km/s, mi/s
    """
    if unit == "m/s":
        return value
    elif unit == "ft/s":
        return value * 0.3048       # 1 ft = 0.3048 m
    elif unit == "km/s":
        return value * 1000         # 1 km = 1000 m
    elif unit == "mi/s":
        return value * 1609.34      # 1 mile = 1609.34 m
    else:
        print("Unsupported velocity unit.")
        return None


# Function 2: Convert acceleration to m/s^2
def convert_acceleration(value, unit):
    """
    Convert acceleration to meters per second squared (m/s^2)
    Supported units: m/s^2, ft/s^2, km/s^2, mi/s^2
    """
    if unit == "m/s^2":
        return value
    elif unit == "ft/s^2":
        return value * 0.3048       # 1 ft/s^2 = 0.3048 m/s^2
    elif unit == "km/s^2":
        return value * 1000         # 1 km/s^2 = 1000 m/s^2
    elif unit == "mi/s^2":
        return value * 1609.34      # 1 mi/s^2 = 1609.34 m/s^2
    else:
        print("Unsupported acceleration unit.")
        return None


# Function 3: Determine motion type
def motion_type(v, a):
    """
    Determine the type of motion based on velocity and acceleration
    Rules:
    - v > 0 and a = 0 → "Uniform Motion"
    - v > 0 and a > 0 → "Accelerated Motion"
    - v > 0 and a < 0 → "Decelerated Motion"
    - v = 0 → "At Rest"
    """
    if v == 0:
        return "At Rest"
    elif v > 0 and a == 0:
        return "Uniform Motion"
    elif v > 0 and a > 0:
        return "Accelerated Motion"
    elif v > 0 and a < 0:
        return "Decelerated Motion"
    else:
        return "Unknown Motion"


# --- Main Program ---

# Step 1: Input velocity
v_value = float(input("Enter velocity value: "))
v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

# Step 2: Input acceleration
a_value = float(input("Enter acceleration value: "))
a_unit = input("Enter acceleration unit (m/s^2, ft/s^2, km/s^2, mi/s^2): ")

# Step 3: Convert to SI units
v_si = convert_velocity(v_value, v_unit)      # Convert velocity
a_si = convert_acceleration(a_value, a_unit)  # Convert acceleration

# Step 4: Determine motion type
motion = motion_type(v_si, a_si)

# Step 5: Display results
print("\n--- Results ---")
print(f"Velocity = {v_si:.3f} m/s")
print(f"Acceleration = {a_si:.3f} m/s^2")
print(f"Motion Type = {motion}")
