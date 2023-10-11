Command: nems-quickfix
======================

Update all components to the latest rolling release and apply all
available patches and fixes to NEMS Linux.

If you're experiencing an issue which has been patched, simply run this
command to ensure your NEMS server receives and installs the patch in
one quick command.

``sudo nems-quickfix``

If you ran a patch previously that has failed, you can reset the patch state and re-run the patch as follows:

``sudo nems-quickfix --reset PATCHNUM`` where ``PATCHNUM`` is the patch number to reset.
