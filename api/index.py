from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer, VerticalBarsDrawer, HorizontalBarsDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
import io

app = FastAPI(title="QR Generator API")

# Add CORS to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QRRequest(BaseModel):
    data: str
    fg_color: str = "#000000"
    bg_color: str = "#ffffff"
    style: str = "square"

def hex_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    return (0, 0, 0)

@app.post("/api/generate")
async def generate_qr(req: QRRequest):
    # Parse RGB colors
    fg_rgb = hex_to_rgb(req.fg_color)
    bg_rgb = hex_to_rgb(req.bg_color)
    
    # Configure QR
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=12,
        border=3
    )
    qr.add_data(req.data)
    
    # Select module drawer based on requested style
    drawer = SquareModuleDrawer()
    if req.style == "circle":
        drawer = CircleModuleDrawer()
    elif req.style == "rounded":
        drawer = RoundedModuleDrawer()
    elif req.style == "vertical":
        drawer = VerticalBarsDrawer()
    elif req.style == "horizontal":
        drawer = HorizontalBarsDrawer()

    color_mask = SolidFillColorMask(front_color=fg_rgb, back_color=bg_rgb)
    
    # Generate image
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=drawer,
        color_mask=color_mask
    )
    
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    
    return Response(content=buf.getvalue(), media_type="image/png")
