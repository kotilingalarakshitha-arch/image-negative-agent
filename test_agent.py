from agent import make_negative

# Load an input image
with open("input.jpg", "rb") as f:
    img_bytes = f.read()
# add text here #
# Call the function directly
result = make_negative(img_bytes)

# Save the output #
with open("negative.png", "wb") as f:
    f.write(result)
# add text #
print("✅ Negative image saved as negative.png")



