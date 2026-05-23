<script lang="ts">
  import Button from '$lib/components/Button.svelte';
</script>

<div class="mx-auto max-w-md p-8">
  <h1 class="text-2xl font-semibold">Connexion</h1>
  <form class="mt-6 space-y-4">
    <input class="w-full rounded-md border border-slate-700 bg-surface-900 px-3 py-2 light:border-slate-300 light:bg-white" placeholder="email@company.com" />
    <input class="w-full rounded-md border border-slate-700 bg-surface-900 px-3 py-2 light:border-slate-300 light:bg-white" placeholder="Mot de passe" type="password" />
    <Button type="submit">Se connecter</Button>
  </form>
  <div class="mt-6 grid gap-2 text-sm text-slate-400">
    <button class="text-left">OIDC</button>
    <button class="text-left">SAML</button>
    <button class="text-left">Microsoft Entra ID</button>
    <button class="text-left">Google Workspace</button>
    <button class="text-left">Keycloak</button>
  </div>
</div>
