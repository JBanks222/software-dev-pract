document.querySelectorAll('.btndelete').forEach((button) => {
    button.addEventListener('click', () => {
        const id = button.dataset.imageId;

        if (!id) {
            return;
        }

        if (!confirm('Are you sure you want to delete this image?')) {
            return;
        }

        fetch(`/delete/${id}`, {
            method: 'DELETE'
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.success) {
                    location.reload();
                    return;
                }

                alert(data.error || 'Delete failed');
            })
            .catch(() => {
                alert('Delete failed');
            });
    });
});