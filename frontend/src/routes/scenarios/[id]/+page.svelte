<script lang="ts">
  import DataTable from '$lib/components/DataTable.svelte';
  import Panel from '$lib/components/Panel.svelte';

  const columns = ['planned time', 'sender', 'recipient', 'stimulus type', 'message preview', 'attachment', 'delivery channel'];
  const rows = [
    { 'planned time': '00:05:00', sender: 'SOC', recipient: 'Crisis cell', 'stimulus type': 'chat message', 'message preview': 'EDR alerts are increasing...', attachment: 'alert.png', 'delivery channel': 'public_channel' }
  ];
</script>

<div class="grid gap-4 p-4 xl:grid-cols-[1fr_360px]">
  <section class="space-y-4">
    <Panel title="Spreadsheet editor" dense>
      <DataTable {columns} {rows} />
    </Panel>
    <Panel title="Drag-and-drop uploads">
      <div class="grid h-32 place-items-center border border-dashed border-slate-700 text-sm text-slate-400 light:border-slate-300">Drop images, PDFs, videos or documents</div>
    </Panel>
  </section>
  <aside class="space-y-4">
    <Panel title="Media browser">
      <div class="grid grid-cols-2 gap-2 text-xs">
        <div class="grid h-24 place-items-center bg-slate-800 light:bg-slate-100">PDF</div>
        <div class="grid h-24 place-items-center bg-slate-800 light:bg-slate-100">Video</div>
      </div>
    </Panel>
    <Panel title="AI agents">
      <div class="text-sm text-slate-400">Journalist, Customer, Employee</div>
    </Panel>
  </aside>
</div>
