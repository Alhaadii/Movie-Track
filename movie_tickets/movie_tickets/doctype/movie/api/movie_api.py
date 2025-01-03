import frappe

@frappe.whitelist(allow_guest=True)
def get_movies():
    """Fetch all movies with specified fields."""
    return frappe.get_all(
        "Movie",
        fields=["name", "title", "poster", "director", "released_date"]
    )
@frappe.whitelist(allow_guest=True)
def get_all_movies():
    """Fetch all movies with all fields."""
    return frappe.db.sql("SELECT name, owner,title, poster, director, released_date,synopsis FROM tabMovie ", as_dict=True)


@frappe.whitelist()
def add_movie(title, director, released_date, poster_url=None):
    """Create a new movie record."""
    if not title or not director or not released_date:
        frappe.throw("Title, Director, and Released Date are required fields.")
    
    movie = frappe.get_doc({
        "doctype": "Movie",
        "title": title,
        "poster": poster_url,  # Allow null
        "director": director,
        "released_date": released_date
    })
    movie.insert()
    frappe.db.commit()
    return movie.name

@frappe.whitelist()
def delete_movie(movie_id):
    """Delete a movie record."""
    frappe.delete_doc("Movie", movie_id)
    frappe.db.commit()
    return {"message": f"Movie {movie_id} deleted successfully."}
