class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        cls(photos_count / 4)

    def add_photo(self, label: str):
        for i in range(self.pages):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1}" \
                       f" slot {self.photos[i].index(label) + 1}"
        return "No more free spots"

    def display(self):
        result = ''
        dashes = f"{'-' * 11}\n"
        result += dashes
        for page in self.photos:
            to_add = ' '.join(['[]' for _ in range(len(page))])
            result += to_add + '\n'
            result += dashes
        return result[:-1]


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
