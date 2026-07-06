
from flask import Blueprint, render_template
dashboard_bp=Blueprint("dashboard",__name__)
@dashboard_bp.get("/")
def home():
    stats={"shipments":0,"customers":0,"drivers":0,"warehouses":0}
    return render_template("dashboard/index.html",stats=stats)
