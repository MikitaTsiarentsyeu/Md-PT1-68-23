l = [4,23,2,4,6,7,5,3,2,4,7,87,4,7]

for m_i in range(len(l)-1):
    current_i = m_i
    for i in range(current_i+1, len(l)):
        if l[i]<l[m_i]:
            m_i = i

    l[current_i], l[m_i] = l[m_i], l[current_i]

    print(l)
