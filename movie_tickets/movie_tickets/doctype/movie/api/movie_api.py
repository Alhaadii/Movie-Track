import frappe

@frappe.whitelist()
def get_movies():
    """Fetch all movies with specified fields."""
    return frappe.get_all(
        "Movie",
        fields=["name", "title", "poster", "director", "released_date"]
    )

@frappe.whitelist()
def add_movie(title, director, released_date, poster=None):
    """Create a new movie record."""
    if not title or not director or not released_date:
        frappe.throw("Title, Director, and Released Date are required fields.")
    
    movie = frappe.get_doc({
        "doctype": "Movie",
        "title": title,
        "poster": poster,  # Allow null
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
