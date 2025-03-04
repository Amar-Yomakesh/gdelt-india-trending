from gdeltdoc import GdeltDoc, Filters


f = Filters(
    country="IN",
    start_date="2025-03-03",
    end_date="2025-03-04",
    theme="EDUCATION"
)

gd = GdeltDoc()
articles = gd.article_search(f)
timeline = gd.timeline_search("timelinevolraw", f)
print(timeline)
