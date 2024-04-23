﻿using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
using FakeStoreApi.Models;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;

namespace FakeStoreApi.Controllers
{
    [ApiController] // Indica que el controlador responde a peticiones HTTP y que los resultados de los métodos de acción se escribirán directamente en la respuesta HTTP.
    [Route("api/[controller]")] // Especifica la ruta base para las solicitudes HTTP que serán manejadas por este controlador. En este caso, la ruta base será "/api/FakeStore".
    public class FakeStoreController : ControllerBase 
    {
        private readonly HttpClient _httpClient; // Declara un campo privado readonly para almacenar una instancia de HttpClient.

        #region ¿Qué es http client?

        /*
         * La instancia de HttpClient en este contexto se utiliza para realizar solicitudes HTTP al servicio Fake Store API. 
         * Cuando se crea una instancia de HttpClient en el constructor del controlador FakeStoreController, se configura con una dirección base que apunta al endpoint del API (https://api.escuelajs.co/api/v1/). 
         * Esta dirección base se utiliza como punto de partida para todas las solicitudes HTTP realizadas por ese HttpClient.
         */

        #endregion

        public FakeStoreController(IHttpClientFactory httpClientFactory) // Constructor del controlador que recibe una instancia de IHttpClientFactory. ASP.NET Core proporcionará automáticamente una implementación de IHttpClientFactory cuando se instancie el controlador.
        {
            _httpClient = httpClientFactory.CreateClient(); // Crea una instancia de HttpClient utilizando el IHttpClientFactory.
            _httpClient.BaseAddress = new Uri("https://api.escuelajs.co/api/v1/"); // Establece la dirección base del cliente HttpClient para las solicitudes HTTP.
        }

        [HttpGet("products")] // Define un método de acción HTTP GET que responde a las solicitudes HTTP en la ruta "/api/FakeStore/products".
        public async Task<IActionResult> GetProducts() // El método de acción es asincrónico y devuelve un IActionResult.
        {
            var response = await _httpClient.GetAsync("products"); // Realiza una solicitud GET al endpoint "products" del servicio Fake Store API.
            if (response.IsSuccessStatusCode) // Verifica si la solicitud fue exitosa (código de estado HTTP 200-299).
            {
                var productsJson = await response.Content.ReadAsStringAsync(); // Lee el contenido de la respuesta como una cadena JSON.
                var products = JsonConvert.DeserializeObject<List<Product>>(productsJson); // Deserializa la cadena JSON en una lista de objetos Product utilizando Newtonsoft.Json.
                return Ok(products); // Devuelve un resultado HTTP 200 OK con la lista de productos como cuerpo de la respuesta.
            }
            return StatusCode((int)response.StatusCode); // Devuelve un resultado con el código de estado HTTP recibido en la respuesta del servicio Fake Store API.
        }

        // Métodos de acción similares para los endpoints "categories", "products/{id}", "products" (POST), y "products/{id}" (PUT).
        [HttpGet("categories")]
        public async Task<IActionResult> GetCategories()
        {
            var response = await _httpClient.GetAsync("categories");
            if (response.IsSuccessStatusCode)
            {
                var categoriesJson = await response.Content.ReadAsStringAsync();
                var categories = JsonConvert.DeserializeObject<List<Category>>(categoriesJson);
                return Ok(categories);
            }
            return StatusCode((int)response.StatusCode);
        }

        [HttpGet("products/{id}")]
        public async Task<IActionResult> GetProduct(int id)
        {
            var response = await _httpClient.GetAsync($"products/{id}");
            if (response.IsSuccessStatusCode)
            {
                var productJson = await response.Content.ReadAsStringAsync();
                var product = JsonConvert.DeserializeObject<Product>(productJson);
                return Ok(product);
            }
            return StatusCode((int)response.StatusCode);
        }

        [HttpPost("products")] // Atributo que especifica que este método manejará solicitudes HTTP POST en la ruta "/products"
        public async Task<IActionResult> AddProduct(Product product) // Método para agregar un nuevo producto
        {
            // Serializar el objeto product a formato JSON
            var productJson = JsonConvert.SerializeObject(product);
            // Crear un objeto StringContent para incluir el JSON en el cuerpo de la solicitud HTTP
            var content = new StringContent(productJson, System.Text.Encoding.UTF8, "application/json");
            Console.WriteLine(content);

            // Enviar la solicitud HTTP POST al servidor con el JSON del producto en el cuerpo
            var response = await _httpClient.PostAsync("products", content);

            // Verificar si la solicitud se realizó correctamente (código de estado 2xx)
            if (response.IsSuccessStatusCode)
            {
                // Si la solicitud fue exitosa, devolver un código de estado 200 OK
                return Ok();
            }
            else
            {
                // Si la solicitud no fue exitosa, devolver el código de estado recibido del servidor
                return StatusCode((int)response.StatusCode);
            }
        }


        [HttpPut("products/{id}")]
        public async Task<IActionResult> UpdateProduct(int id, Product product)
        {
            var productJson = JsonConvert.SerializeObject(product);
            var content = new StringContent(productJson, System.Text.Encoding.UTF8, "application/json");

            var response = await _httpClient.PutAsync($"products/{id}", content);
            if (response.IsSuccessStatusCode)
            {
                return Ok();
            }
            return StatusCode((int)response.StatusCode);
        }
    }

    
}