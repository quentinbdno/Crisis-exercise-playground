<script lang="ts">
  import Button from '$lib/components/Button.svelte';
  import DataTable from '$lib/components/DataTable.svelte';

  const columns = ['scenario name', 'author', 'creation date', 'number of stimuli', 'number of media files', 'linked AI agents'];
  const rows = [
    { 'scenario name': 'Ransomware supply chain', author: 'Admin', 'creation date': '2026-05-23', 'number of stimuli': 32, 'number of media files': 9, 'linked AI agents': 3 }
  ];
</script>

<div class="p-4">
  <div class="mb-3 flex flex-wrap items-center gap-2">
    <Button>Create scenario</Button>
    <Button variant="ghost">Import</Button>
    <Button variant="ghost">Export</Button>
    <Button variant="ghost">Duplicate</Button>
  </div>
  <DataTable {columns} {rows} />
</div>
