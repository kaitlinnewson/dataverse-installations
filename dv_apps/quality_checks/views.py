from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings
from dv_apps.quality_checks.util_filesize_zero import ZeroFilesizeStats
from dv_apps.quality_checks.util_no_checksum import NoChecksumStats

def view_qc_dashboard(request):
    """
    Display QC dashboard (beginning, only 3 simple measures right now)
    """

    info_dict = dict(size_zero_stats=ZeroFilesizeStats.get_basic_stats(),
                     checksum_stats=NoChecksumStats.get_basic_stats())

    return render(request,
                  'qc_dashboard.html',
                  info_dict)


def view_filesize_zero_local_list(request):
    """
    List local files with size zero or null
    """
    dfiles = ZeroFilesizeStats.get_local_files_bad_size()
    dataset_ids = list(set([df.dvobject.owner_id for df in dfiles]))
    num_datasets = len(dataset_ids)

    info_dict = dict(dfiles=dfiles,
                     num_datasets=num_datasets,
                     subtitle='Local files with size zero or null',
                     installation_url=settings.DATAVERSE_INSTALLATION_URL)

    return render(request,
                  'filesize_zero_local_list.html',
                  info_dict)


def view_no_checksum_list(request):
    """
    List of all files with no checksum
    """
    dfiles = NoChecksumStats.get_files_no_checksum()
    dataset_ids = list(set([df.dvobject.owner_id for df in dfiles]))
    num_datasets = len(dataset_ids)

    info_dict = dict(dfiles=dfiles,
                     num_datasets=num_datasets,
                     subtitle='Files without Checksum values',
                     installation_url=settings.DATAVERSE_INSTALLATION_URL)

    return render(request,
                  'filesize_zero_local_list.html',
                  info_dict)
