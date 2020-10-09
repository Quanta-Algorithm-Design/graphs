#include <iostream>
#include <vector>
#include <unordered_map>

template <typename T>
struct Node
{
    std::vector< Node<T>* > adj;
    T data;
};

template <typename T>
void dfs_visit(Node<T> *start, std::unordered_map< Node<T>*, Node<T>* > &parent)
{
    for (auto *vertex : start->adj)
    {
        if (parent.find(vertex) == parent.end())
        {
            parent.insert({vertex, start});
            dfs_visit(vertex, parent);
        }
    }
}

template <typename T>
void dfs(const std::vector< Node<T>* > &nodes)
{
    std::unordered_map<Node<T>*, Node<T>*> parent;
    for (auto *vertex : nodes)
    {
        if (parent.find(vertex) == parent.end())
        {
            parent.insert({vertex, nullptr});
            dfs_visit(vertex, parent);
        }
    }

    std::cout << "child->parent pairs:\n\n";
    for (auto p : parent)
    {
        if (p.second != nullptr)
            std::cout << p.first->data << "->" << p.second->data << "\n";
        else
            std::cout << p.first->data << "->" << "NULL\n";
    }
}

int main()
{
    auto *a = new Node<char>, *b = new Node<char>, *c = new Node<char>, *d = new Node<char>,
        *e = new Node<char>, *f = new Node<char>, *g = new Node<char>;
    a->data = 'a';
    b->data = 'b';
    c->data = 'c';
    d->data = 'd';
    e->data = 'e';
    f->data = 'f';
    g->data = 'g';
    a->adj.push_back(b);
    a->adj.push_back(c);
    c->adj.push_back(a);
    b->adj.push_back(c);
    c->adj.push_back(d);
    d->adj.push_back(a);
    b->adj.push_back(e);
    e->adj.push_back(f);
    f->adj.push_back(g);
    g->adj.push_back(e);
    std::vector< Node<char>* > nodes {a, b, c, d, e, f, g};
    dfs(nodes);
}