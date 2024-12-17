from typing import Any
from blog.models import Post, Category
from django.core.management.base import BaseCommand
import random

class Command(BaseCommand):
    help="this command insert post data"
    
    def handle(self, *args:Any, **options:Any):
        #delete exitsing data
        Post.objects.all().delete()
        
        titles=[
"The Python Chronicles",
"Whispering Code",
"Beyond the Algorithm",
"The Django Odyssey",
"Pixels of Imagination",
"Data Tales Unveiled",
"The Debugger's Diary",
"AI: Friend or Foe?",
"The Architect's Notebook",
"Algorithms and Anecdotes",
"Zero to App Hero",
"Shadows of Cybersecurity",
"JavaScript Unleashed",
"Threads of Asynchrony",
"The Cloud Symphony",
"MySQL Mysteries",
"Infinite Loops",
"Framework Wars",
"Git & the Art of Version Control",
"Bytes of History",
"Debugging Life",
"The Frontend Canvas",
"Code & Coffee",
"The Compiler’s Whisper",
"Loops, Lists, and Life Lessons"
]

        contents=[
"    Discover Python’s journey from basics to advanced topics. Learn programming through engaging stories, real-world examples, and practical coding exercises.",
"Explore the human side of programming—how creativity, collaboration, and problem-solving shape the tech we use, making coding an art beyond algorithms.",
"Follow a beginner-friendly path through Django. Learn building web apps step-by-step with tutorials, tips, and challenges tailored for developers.",
"Dive into the artistic side of design, exploring how creativity turns ideas into digital masterpieces, inspiring innovation across websites and apps.",
"Journey into the world of data analysis and visualization, discovering insights, creating impactful charts, and unlocking stories hidden in numbers.",
"Chronicles of a coder tackling complex bugs, learning life lessons along the way, and discovering that problem-solving is more rewarding than it seems.",
"An exploration of artificial intelligence’s role in society—how it helps humanity and the challenges we face as machines become smarter than ever.",
"Blueprints for software success: discover principles of scalable design, robust architecture, and tools that help craft systems capable of growing.",
"Blending technical knowledge with quirky stories, this book introduces algorithms that shape our digital lives in practical, fascinating, and humorous ways.",
"Learn to build your first app with minimal resources. From planning to execution, this beginner’s guide simplifies the journey to your first launch.",
"A thrilling dive into the dark world of hackers, showing how cybersecurity experts battle relentless threats to protect the invisible networks.",
"Uncover the true power of JavaScript, transforming from a simple scripting language into a robust toolkit for creating modern and engaging apps.",
"Explore asynchronous programming’s intricacies, from promises to threads, through practical examples showcasing how it revolutionizes performance.",
"A poetic journey through cloud computing’s wonders—learn how data flows, scales, and secures, creating harmony for businesses in the digital age.",
"Navigate the enigmatic world of MySQL, solving database dilemmas with tricks, tips, and queries to manage and retrieve data effectively.",
"A philosophical exploration of coding loops and life cycles, offering insights into repetitive patterns, infinite possibilities, and breaking stagnation.",
"An unbiased look at modern development frameworks—Django, Flask, React—showcasing strengths, weaknesses, and ideal use cases for informed decisions",
"A step-by-step guide to mastering Git, navigating commits, branches, and merges, while appreciating the beauty of organized, collaborative development.",
"A journey through the evolution of computing, from the first algorithms to modern AI, showing how history shaped today’s technological landscape.",
"Parallel lessons in programming and personal growth, teaching how to identify issues, solve problems, and navigate life’s inevitable bugs with patience.",
"A colorful dive into frontend development, learning HTML, CSS, and JavaScript to design interfaces that are both functional and aesthetically pleasing.",
"A casual guide for programmers tackling daily challenges, filled with tips, anecdotes, and wisdom brewed for those late-night coding sessions.",
"A story that unravels the magic behind programming languages, exploring how compilers translate code into actions machines can execute with precision.",
"A thoughtful mix of coding tutorials and personal anecdotes, showing how programming concepts mirror everyday life in unexpected and inspiring ways."
]

        img_urls=[
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400",
    "https://picsum.photos/id/21/800/400",
    "https://picsum.photos/id/22/800/400",
    "https://picsum.photos/id/23/800/400",
    "https://picsum.photos/id/24/800/400",
    "https://picsum.photos/id/25/800/400"    
]


        categories= Category.objects.all()
        for title,content,img_url in zip(titles,contents,img_urls):
            category= random.choice(categories)
            Post.objects.create(title=title,content=content,img_url=img_url,category=category)

        self.stdout.write(self.style.SUCCESS("Data inserted successfully"))
