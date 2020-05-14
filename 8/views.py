from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_blank_len = len(text.replace(" ", ""))
    modi_text = text.replace(".", " ").replace(",", " ").replace("?", " ").replace("!", " ")
    final_text = modi_text.replace("  ", " ")
    word_split = final_text.split(" ")
    if "" in word_split:
        word_len = len(word_split) - 1
    else:
        word_len = len(word_split)

    return render(request, 'result.html', {
        'total_len' : total_len,
        'text' : text,
        'no_blank_len' : no_blank_len,
        'word_len' : word_len,
    })

