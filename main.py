from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from managers.sportclub_controller import router as sportclub_router

app = FastAPI(title="Sport Club Management")

# Templates directory
templates = Jinja2Templates(directory="views/templates")

# Include the existing API router
app.include_router(sportclub_router, prefix="/api")


# -------------------- Home Page --------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# -------------------- Members Page --------------------
@app.get("/members", response_class=HTMLResponse)
def members_page(request: Request):
    return templates.TemplateResponse("members.html", {"request": request})


# -------------------- Events Page --------------------
@app.get("/events", response_class=HTMLResponse)
def events_page(request: Request):
    return templates.TemplateResponse("events.html", {"request": request})


# -------------------- Subscriptions Page --------------------
@app.get("/subscriptions", response_class=HTMLResponse)
def subs_page(request: Request):
    return templates.TemplateResponse("subscriptions.html", {"request": request})
