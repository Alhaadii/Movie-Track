import frappe



# Define a function named get_movies that returns all movies with specified fields.
@frappe.whitelist(allow_guest=True)
def get_movies():
    return frappe.get_all(
        "Movie",
        fields=["name", "title", "poster", "director", "released_date"]
    )


# Define a function named add_movie that takes title, director, and released_date as parameters and creates a new movie record.
@frappe.whitelist()
def add_movie(title, director, released_date, poster=None):
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



# Define a function named delete_movie that takes movie_id as a parameter and deletes the corresponding movie record.
@frappe.whitelist(allow_guest=True)
def delete_movie(movie_id):
    frappe.delete_doc("Movie", movie_id)
    frappe.db.commit()
    return {"message": f"Movie {movie_id} deleted successfully."}