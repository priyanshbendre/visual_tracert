# Visual Tracert

Visualize the route traced by the packet when we use traceroute

### Installation

Install [ipinfo](https://ipinfo.io) library to convert ip address to cities. Create account and get access token for free 50,000 requests per month. (add in line)


```
pip install ipinfo
```

And install [gmplot](https://pypi.org/project/gmplot/) library to plot the co-ordinates on the map

```
pip install gmplot
```

### Execution

Run tracert.py file from terminal (default traceroute: google.com)
(change traceroute location on line 28)

(Will create traceroute.txt and an HTML file with map)