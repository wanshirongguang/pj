
from flask import Blueprint

#1.蓝图的名称
bp = Blueprint("bookbp",import_name=__name__,subdomain="book")

@bp.route("/login/")
def login():
    return "book success"
