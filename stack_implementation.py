{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2bac447a",
   "metadata": {},
   "outputs": [],
   "source": [
    "class stack: \n",
    "  def __init__(self):\n",
    "    self.x=[]\n",
    "  def isEmpty(self):\n",
    "    return self.x==[]\n",
    "  def push(self,element):\n",
    "    self.x.append(element)\n",
    "  def pop (self): \n",
    "    return self.x.pop()\n",
    "  def size (self):\n",
    "    return len(self.x)\n",
    "\n",
    "tickets=stack()\n",
    "no_seats=int(input(\"enter no of seats\"))\n",
    "\n",
    "for i in range (no_seats): \n",
    "  tickets.push(input(\"enter passenger name = \"))\n",
    "  print(\"your seat no is \",no_seats-i)\n",
    "print(\"seats occupied by =\") \n",
    "for i in range (no_seats):\n",
    "  print(tickets.pop())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "805397f6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
