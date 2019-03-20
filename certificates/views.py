from flask import Blueprint, render_template, request, flash
from .connection import db, Certificate

views = Blueprint("routes", __name__)


@views.route("/")
def index():
    return render_template("index.html")


@views.route("/certificate")
def certificate():
    token = request.args.get("token")

    if not token:
        return render_template("not_found.html")

    cert = Certificate.query.filter_by(token=token).first()

    if not cert:
        return render_template("not_found.html")

    return render_template("certificate.html", cert=cert)


@views.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        if request.form.get("type") == "delete":
            id_ = request.form.get("id")
            cert = Certificate.query.filter_by(id=id_).first()
            if cert:
                db.session.delete(cert)
                db.session.commit()
        elif request.form.get("type") == "create":
            token_exists = Certificate.query.filter_by(token=request.form.get("token")).first()
            if token_exists:
                flash('Token already exists')
            else:
                cert = Certificate(
                    person=request.form.get("person"),
                    type=request.form.get("type"),
                    issue_date=request.form.get("date") or None,
                    token=request.form.get("token"),
                    link=request.form.get("link") or None,
                    approved_by=request.form.get("approved_by"),
                    description=request.form.get("description")
                )
                db.session.add(cert)
                db.session.commit()

    page = int(request.args.get('page', 1))
    count = Certificate.query.count()
    certificates = Certificate.query.offset((page - 1) * 50).limit(50).all()
    return render_template("admin.html", count=count, certificates=certificates, current=page)


@views.route('/login', methods=["GET", "POST"])
def login():
    pass
