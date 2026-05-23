<script lang="ts">
  import Button from '$lib/components/Button.svelte';
</script>

<div class="mx-auto max-w-md p-8">
  <h1 class="text-2xl font-semibold">Accept invitation</h1>
  <div class="mt-6 space-y-4">
    <input class="w-full rounded-md border border-slate-700 bg-surface-900 px-3 py-2 light:border-slate-300 light:bg-white" placeholder="Invitation token" />
    <input class="w-full rounded-md border border-slate-700 bg-surface-900 px-3 py-2 light:border-slate-300 light:bg-white" placeholder="Password" type="password" />
    <Button>Activate account</Button>
  </div>
</div>
