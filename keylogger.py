import keyboard

file = open("output.txt", "w")

while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        file.write(f"Key pressed: {event.name}\n")
    if event.event_type == keyboard.KEY_UP:
        file.flush()
        print("Key pressed: ", event.name)
