from flask import render_template, redirect, url_for
from sqlalchemy import desc
from ..models import Comment
from .. import db

from . import home
from .forms import CommentForm, EditCommentForm


@home.route("/", methods=["GET", "POST"])
def index():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(name=form.name.data, content=form.content.data)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for("home.index"))
    comments = Comment.query.order_by(desc(Comment.created_at)).all()
    return render_template(
        "home/index.html", title="Home", form=form, comments=comments
    )


@home.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    comments = Comment.query.all()
    comment = Comment.query.get(id)
    form = EditCommentForm(name=comment.name, content=comment.content)
    if form.validate_on_submit():
        comment.name = form.name.data
        comment.content = form.content.data
        db.session.commit()

        return redirect(url_for("home.index"))

    return render_template(
        "home/index.html", title="Edit", form=form, comments=comments
    )


@home.route("/delete/<int:id>")
def delete(id):
    comment = Comment.query.get(id)
    db.session.delete(comment)
    db.session.commit()

    return redirect(url_for("home.index"))
