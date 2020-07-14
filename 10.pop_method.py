subscribers = ['nusrat@example.com', 'maya@example.com', 'shoshi@example.com']

print(subscribers)

popped_sub = subscribers.pop()

print(subscribers)
print(popped_sub)

subscribers = ['nusrat@example.com', 'maya@example.com', 'shoshi@example.com']
first_sub = subscribers.pop(0)
print("first " + first_sub)

subscribers = ['nusrat@example.com', 'maya@example.com', 'shoshi@example.com']
print(subscribers)

subscribers.remove('maya@example.com')
print(subscribers)

subscribers = ['nusrat@example.com', 'maya@example.com', 'shoshi@example.com']
print(subscribers)
sub_by_mistake = 'nusrat@example.com'
subscribers.remove(sub_by_mistake)
print(subscribers)
