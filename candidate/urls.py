from django.urls import include, path

from . import views

urlpatterns = [



	path('', view=views.app_can, name='app_can'),
	# path('create/', view=views.bookadmin_index_view, name='create_book_record'),
	# path('delete/<int:id>/', view=views.bookadmin_delete_book, name='delete_book_record'),
	# path('edit/<int:id>/', view=views.bookadmin_update_book, name='update_book_record'),

	# path('details/<int:id>', view=views.details, name='details')
]
