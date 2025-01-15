# -*- coding: utf-8 -*-
{
    "name": "Academy System Information Management v1.2",
    "summary": "Create and manage students for your academy",
    "description": """
Create and manage students for your academy.
    """,
    "author": "muhammad Rizky",
    "category": "Education",
    "license": "AGPL-3",
    "website": "masrizky.online",
    "version": "1.0",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/course.xml",
        "views/session.xml",
        "views/attendee.xml",
        "views/partner.xml",
        "wizard/create_attendee.xml",
    ],
    "images": ["static/images/banner.png", "static/description/icon.png"],
    "installable": True,
    "application": True,  # Ini menunjukkan bahwa modul yang dibuat adalah sebuah aplikasi.
    "auto_install": False,
}
