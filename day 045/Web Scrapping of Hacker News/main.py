from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

content = response.text
soup = BeautifulSoup(content, "html.parser")
#print(soup.title)

topic = soup.find_all(class_="titlelink")
#print(topic.get_text())
topic_name = []
topic_link = []
for t in topic:
    name = t.get_text()
    topic_name.append(name)
    link = t.get("href")
    topic_link.append(link)

#

topic_scores = [int(score.get_text().split(" ")[0]) for score in soup.find_all(class_="score")]
#print(topic_scores)

max_score_index = topic_scores.index(max(topic_scores))
print(topic_name[max_score_index])
print((topic_link[max_score_index]))
print(topic_scores[max_score_index])
