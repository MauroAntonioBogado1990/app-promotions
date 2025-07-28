<script lang="ts">
  import { onMount } from 'svelte';
  import maplibregl from 'maplibre-gl';
  import Ventas from './Ventas.svelte';
  import Mapas from './Mapas.svelte';
  import CrearUsuario from './CrearUsuario.svelte'
  let mapContainer: HTMLDivElement;
  let latitude = -34.61;
  let longitude = -58.38;
  let currentSection: 'bienvenida' | 'mapa' | 'ventas' | 'compras' = 'bienvenida';

  let email = "";
  let password = "";
  let serverUrl = "http://localhost:8000";
  let dbname = "";
  let error = "";
  let success = "";

  onMount(() => {
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        latitude = pos.coords.latitude;
        longitude = pos.coords.longitude;
      },
      (err) => console.error("No se pudo obtener ubicación:", err)
    );
  });

  function loadMap() {
    

    new maplibregl.Marker()
      .setLngLat([longitude, latitude])
      .setPopup(new maplibregl.Popup().setText("Tu ubicación"))
      .addTo(map);
  }

  $: if (currentSection === 'mapa' && mapContainer) {
    setTimeout(() => loadMap(), 100);
  }

  async function login() {
    error = "";
    success = "";

    try {
      const res = await fetch(`${serverUrl}/api/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password, url: "http://localhost:8069", db: dbname }),
      });

      const result = await res.json();
      if (result.uid) {
        localStorage.setItem("odoo_uid", result.uid.toString());
        success = "✅ Usuario logueado correctamente";
      } else {
        error = "❌ Credenciales inválidas o base de datos incorrecta";
      }
    } catch (err) {
      error = "❌ Error inesperado: " + err.message;
    }
  }
</script>

<!-- 🧭 Navbar -->
<nav class="navbar">
  <div class="logo">🚚 Conexión Camiones ERP</div>
  <div class="tabs">
    <button on:click={() => currentSection = 'bienvenida'}>Inicio</button>
    <button on:click={() => currentSection = 'mapa'}>Mapa</button>
    <button on:click={() => currentSection = 'ventas'}>Ventas</button>
    <button on:click={() => currentSection = 'compras'}>Compras</button>
  </div>
</nav>

<!-- 🧩 Secciones -->
{#if currentSection === 'bienvenida'}
  <section class="section">
    <h1>Bienvenido</h1>
    <form class="login-form" on:submit|preventDefault={login}>
      <label for="email">Correo electrónico</label>
      <input id="email" type="email" bind:value={email} required placeholder="ejemplo@correo.com" />

      <label for="password">Contraseña</label>
      <input id="password" type="password" bind:value={password} required placeholder="••••••••" />

      <button type="submit">Ingresar</button>
      <h6>Si no posee cuenta, crear cuenta</h6> 
      <button on:click={() => currentSection = 'crear_usuario'}>Crear Cuenta</button>
    </form>

    {#if success}
      <p style="color:green">{success}</p>
    {/if}
    {#if error}
      <p style="color:red">{error}</p>
    {/if}
  </section>
{/if}

{#if currentSection === 'mapa'}
  <Mapas />
{/if}

{#if currentSection === 'ventas'}
  <Ventas />
{/if}

{#if currentSection === 'crear_usuario'}
  <CrearUsuario />
{/if}

{#if currentSection === 'compras'}
  <section class="section">
    <h2>Compras</h2>
    <p>Podés listar solicitudes de compra, proveedores, etc. conectados a tu ERP 📦</p>
  </section>
{/if}

<style>
 
</style>