import re


def clean_markdown(text):
	text = re.sub(r'^\s*#{2,6}\s+', '', text, flags=re.MULTILINE)
	text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
	text = re.sub(r'`([^`]+)`', r'\1', text)
	text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
	text = re.sub(r'^\s*[-*]\s+', '- ', text, flags=re.MULTILINE)
	text = re.sub(r'^\s*\|.*\|\s*$', '', text, flags=re.MULTILINE)
	text = re.sub(r'^\s*[-| :]+\s*$', '', text, flags=re.MULTILINE)
	return text.strip()