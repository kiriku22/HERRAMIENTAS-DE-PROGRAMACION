// todo.service.ts
import { Injectable } from '@angular/core';
import { Todo } from '../models/todo.models.component';

@Injectable({
  providedIn: 'root'
})
export class TodoService {
  private todos: Todo[] = [
    { id: 1, title: 'Hacer la compra', completed: false },
    { id: 2, title: 'Estudiar para el examen', completed: true },
    { id: 3, title: 'Ir al gimnasio', completed: false }
  ];

  constructor() {}

  getTodos(): Todo[] {
    return this.todos;
  }

  addTodo(todo: Todo): void {
    this.todos.push(todo);
  }

  deleteTodo(id: number): void {
    this.todos = this.todos.filter(todo => todo.id !== id);
  }
}