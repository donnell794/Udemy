// --- Directions
// Implement classes Node and Linked Lists
// See 'directions' document

class Node {
  constructor(data, next = null){
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor(){
    this.head = null;
  }

  insertFirst(data){
    this.head = new Node(data, this.head);
  }

  size(){
    let count = 0;
    let temp = this.head;
    while(temp){
      count++;
      temp = temp.next;
    }
    return count;
  }

  getFirst(){
    return this.head;
  }

  getLast(){
    if(!this.head){
      return null;
    }
    let temp = this.head;
    while(temp){
      if(!temp.next){
        return temp;
      }
      temp = temp.next;
    }
    //return temp;
  }

  clear(){
    this.head = null;
    //this.head.next = null;
  }

  removeFirst(){
    if(!this.head){
      return;
    }
    this.head = this.head.next;
  }

  removeLast(){
    if(!this.head){
      return;
    }
    if(!this.head.next){
      this.clear();
      return;
    }
    let temp = this.head;
    let prev = null;
    while(temp){
      if(!temp.next){
        //temp = null;
        prev.next = null;
        break;
      }
      prev = temp;
      temp = temp.next;
    }
  }

  insertLast(data){
    const temp = this.getLast();
    if(temp){
      temp.next = new Node(data);
    }else{
      this.head = new Node(data);
    }
  }

  getAt(n){
    let count = 0;
    let temp = this.head;
    while(temp){
      if(count === n){
        return temp;
      }
      count++;
      temp = temp.next;
    }
    return null;
  }

  removeAt(n){
    if(!this.head){
        return;
    }
    if(n === 0){
      this.head = this.head.next;
    }
    let prev = this.getAt(n - 1);
    if(!prev || !prev.next){
      return;
    }
    prev.next = prev.next.next;
  }

  insertAt(data, n){
    if(!this.head){
      this.head = new Node(data);
      return;
    }
    if(n === 0){
      this.head = new Node(data, this.head);
      return;
    }
    const prev = this.getAt(n - 1) || this.getLast();
    const node = new Node(data, prev.next);
    prev.next = node;
  }

  forEach(fn){
    let temp = this.head;
    let count = 0;
    while(temp){
      fn(temp, count);
      temp = temp.next;
      count++;
    }
  }

  *[Symbol.iterator](){
    let node = this.head;
    while(node){
      yield node;
      node = node.next;
    }
  }
}

module.exports = { Node, LinkedList };
