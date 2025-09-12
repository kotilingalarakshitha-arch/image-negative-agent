from agno.agent import Agent
from PIL import Image, ImageOps
import io

# Define a plain Python function (no @tool)
def make_negative(image_bytes: bytes) -> bytes:
    """Takes an image and returns its negative (inverted colors)."""
    with Image.open(io.BytesIO(image_bytes)) as img:
        # Convert to RGB if needed
        if img.mode not in ('RGB', 'L'):
            img = img.convert('RGB')

        inverted = ImageOps.invert(img)

        # Save inverted image into memory
        buf = io.BytesIO()
        inverted.save(buf, format="PNG")
        return buf.getvalue()

# Create an agent (not really needed here, but you can keep it)
agent = Agent(
    name="ImageNegAgent",
    role="Agent that makes negative images",
    tools=[make_negative],
    model=None   # 👈 ensures no OpenAI calls
)
