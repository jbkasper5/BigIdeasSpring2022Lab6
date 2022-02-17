from myClass import Repo

repo = Repo()
print(repo.owner)
print(repo.creationDate)
repo.addContributor('Mitch')
print(repo.contributors)
