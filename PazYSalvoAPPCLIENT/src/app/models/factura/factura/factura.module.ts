import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';



@NgModule({
  declarations: [],
  imports: [
    CommonModule
  ]
})
export class FacturaModule { }
export class Usuario {
  id: number;
  nombre: string;
  email: string;
  // Otros campos según tus necesidades

  constructor(id: number, nombre: string, email: string) {
    this.id = id;
    this.nombre = nombre;
    this.email = email;
  }
}