<script lang="ts">
  import DataTable from '$lib/components/DataTable.svelte';
  import Panel from '$lib/components/Panel.svelte';

  const columns = ['agent name', 'linked scenarios', 'linked LLM', 'activation status'];
  const rows = [
    { 'agent name': 'Journalist', 'linked scenarios': 4, 'linked LLM': 'OpenAI compatible', 'activation status': 'Active' },
    { 'agent name': 'Customer', 'linked scenarios': 2, 'linked LLM': 'Ollama', 'activation status': 'Paused' }
  ];
</script>

<div class="grid gap-4 p-4 xl:grid-cols-[1fr_460px]">
  <DataTable {columns} {rows} />
  <Panel title="Persona editor">
    <textarea class="h-80 w-full rounded-md border border-slate-700 bg-surface-950 p-3 font-mono text-sm light:border-slate-300 light:bg-white"># Journalist persona
You ask concise, pressure-building questions and request official statements.</textarea>
    <div class="mt-4 grid gap-2 text-sm text-slate-400">
      <div>Model: gpt-compatible-secure</div>
      <div>Behavior: ask follow-up when teams delay public response</div>
    </div>
  </Panel>
</div>
