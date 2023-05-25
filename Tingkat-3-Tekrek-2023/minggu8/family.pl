male(lennart).
male(mike).
male(donald).
male(usain).
male(joar).
male(adam).
male(dan).
male(simon).
female(hillary).
female(elise).
female(lisa).
female(lena).

parent(mike, lennart).
parent(mike, lena).
parent(lennart, donald).
parent(lennart, hillary).
parent(lennart, usain).
parent(lena, adam).
parent(lena, simon).
parent(adam, dan).
parent(donald, lisa).
parent(hillary, joar).
parent(hillary, elise).


child(lisa).
child(joar).
child(elise).
child(dan).
child(simon).

%% predicate rules
father(X,Y) :- male(X),parent(X,Y).
mother(X,Y) :- female(X),parent(X,Y).
son(X,Y) :- male(X),parent(Y,X).
daughter(X,Y) :- female(X),parent(Y,X).

family_children(X, X):-
    child(X).

family_children(X, Child):-
    parent(X,Y),
    family_children(Y, Child).