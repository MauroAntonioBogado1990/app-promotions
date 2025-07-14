<script>
  import Dashboard from './routes/Dashboard.svelte'
  import Inventario from './routes/Inventario.svelte'
  import '../src/dashboard.css';

  let currentPage = 'dashboard'; // cambia esto según navegación
  <script lang="ts">
  const uid = localStorage.getItem("odoo_uid");
  const db = localStorage.getItem("odoo_db");
  const url = localStorage.getItem("odoo_url");
  const email = localStorage.getItem("odoo_email");

  let error = "";
</script>

</script>

{#if currentPage === 'dashboard'}
  <Dashboard />
{:else if currentPage === 'inventario'}
  <Inventario />
{/if}

<style>
  .dashboard {
    padding: 1.5rem;
    font-family: Arial, sans-serif;
  }
  .panel {
    background: #f5f5f5;
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 1rem;
  }
  .panel h2 {
    margin: 0 0 0.5rem 0;
  }
  .nav {
    display: flex;
    gap: 1rem;
  }
  .nav a {
    padding: 0.75rem 1rem;
    background: #2d7fdd;
    color: white;
    text-decoration: none;
    border-radius: 4px;
  }
</style>
