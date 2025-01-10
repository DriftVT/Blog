import os
import datetime
import xml.etree.ElementTree as ET
import xml.dom.minidom

# Configuration: update these as needed
BLOG_TITLE = "DriftVT Blog"
BLOG_LINK = "https://driftvt.github.io/Blog/"
BLOG_DESCRIPTION = "Updates and posts from DriftVT."
POSTS_DIR = "posts"  # Directory containing your HTML post files
RSS_FILE = "rss.xml"  # Output RSS file

def create_rss_feed():
    # Create root elements
    rss = ET.Element('rss')
    rss.set('version', '2.0')
    channel = ET.SubElement(rss, 'channel')
    
    # Add basic channel info
    ET.SubElement(channel, 'title').text = BLOG_TITLE
    ET.SubElement(channel, 'link').text = BLOG_LINK
    ET.SubElement(channel, 'description').text = BLOG_DESCRIPTION

    # Iterate over HTML files in the posts directory
    # Sorted in reverse order to list recent posts first
    for filename in sorted(os.listdir(POSTS_DIR), reverse=True):
        if filename.endswith(".html"):
            file_path = os.path.join(POSTS_DIR, filename)
            # Get the last modified time of the file
            mod_time = os.path.getmtime(file_path)
            pub_date = datetime.datetime.utcfromtimestamp(mod_time).strftime('%a, %d %b %Y %H:%M:%S GMT')
            
            # Use the filename (without extension) as the title
            title = os.path.splitext(filename)[0]
            # Construct the link to the post
            link = f"{BLOG_LINK}posts/{filename}"
            # Placeholder description; customize if needed
            description = f"Read the post: {title}"

            # Create an <item> for each post
            item = ET.SubElement(channel, 'item')
            ET.SubElement(item, 'title').text = title
            ET.SubElement(item, 'link').text = link
            ET.SubElement(item, 'description').text = description
            ET.SubElement(item, 'pubDate').text = pub_date

    return rss

def prettify(elem):
    """Return a pretty-printed XML string for the Element."""
    rough_string = ET.tostring(elem, encoding='utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# Generate the RSS feed
rss_feed = create_rss_feed()
pretty_rss = prettify(rss_feed)

# Write to the RSS file
with open(RSS_FILE, "w", encoding='utf-8') as f:
    f.write(pretty_rss)

print(f"RSS feed generated and saved to {RSS_FILE}")
