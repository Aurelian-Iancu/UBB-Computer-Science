from src.repository.repositoryBook import BookRepoTextFile
from src.repository.repositoryRent import RentRepoTextFile

from src.services.serviceBook import ServiceBook
from src.services.serviceRent import ServiceRent

from ui.console import Console

book_repo = BookRepoTextFile("books.txt")
rent_repo = RentRepoTextFile("rents.txt")

book_service = ServiceBook(book_repo)
rent_service = ServiceRent(rent_repo)

console = Console(book_service, rent_service)

console.start()