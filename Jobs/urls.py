from django.urls import include, path

from . import views

urlpatterns = [



	path('', view=views.bookadmin_index_view, name='bookadmin_index_view'),
	path('create/', view=views.bookadmin_index_view, name='create_book_record'),


	path('add_dept/', view=views.add_dept, name='add_dept'),
	path('add_status/', view=views.add_status, name='add_status'),
	path('add_job_type/', view=views.add_job_type, name='add_job_type'),

	
	path('delete/<int:id>/', view=views.bookadmin_delete_book, name='delete_book_record'),
	path('edit/<int:id>/', view=views.edit, name='edit'),

	path('update/<int:id>/', view=views.update, name='update'),

	path('details/<int:id>', view=views.details, name='details')
]
