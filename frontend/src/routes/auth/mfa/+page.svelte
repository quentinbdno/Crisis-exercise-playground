<script lang="ts">
  import Button from '$lib/components/Button.svelte';
</script>

<div class="mx-auto max-w-md p-8">
  <h1 class="text-2xl font-semibold">MFA setup</h1>
  <div class="mt-6 grid place-items-center border-y border-slate-800 bg-surface-900 p-8 light:border-slate-200 light:bg-white">
    <div class="grid h-40 w-40 place-items-center bg-white text-xs text-slate-900">TOTP QR</div>
  </div>
  <div class="mt-4 space-y-4">
    <input class="w-full rounded-md border border-slate-700 bg-surface-900 px-3 py-2 light:border-slate-300 light:bg-white" placeholder="123456" />
    <Button>Verify</Button>
  </div>
</div>
