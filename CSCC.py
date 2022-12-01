from __future__ import division, print_function, absolute_import
import os
import copy

import re
import glob
import os.path as osp
import warnings


class CSCC(object):
    '''
    CSCC Dataset
    '''
    _junk_pids = [0, -1]
    dataset_dir = 'CSCC'

    def __init__(self, datasets_root = '', verbose = True, relabel=True, combineall=False):
        self.dataset_dir = osp.join(datasets_root, self.dataset_dir)
        # self.dataset_dir = datasets_root
        self.is_video = False
        self.train_dir = osp.join(self.dataset_dir, 'train')
        self.query_dir = osp.join(self.dataset_dir, 'query')
        self.gallery_dir = osp.join(self.dataset_dir, 'test')

        self._check_before_run()
        self.id_label_list = []

        train = self._process_dir(self.train_dir, relabel=True, training=True)
        query = self._process_dir(self.query_dir, relabel=False)
        gallery = self._process_dir(self.gallery_dir, relabel=False)

        if verbose:
            print("=> CSCC loaded")
            self.print_dataset_statistics(train, query, gallery)

        self.train = train
        self.query = query
        self.gallery = gallery


        self.num_train_pids, self.num_train_imgs, self.num_train_cams, self.train_cloths = self.get_imagedata_info( self.train)
        self.num_query_pids, self.num_query_imgs, self.num_query_cams, self.query_cloths = self.get_imagedata_info(self.query)
        self.num_gallery_pids, self.num_gallery_imgs, self.num_gallery_cams, self.gallery_cloths = self.get_imagedata_info(self.gallery)


    def _check_before_run(self):
        """Check if all files are available before going deeper"""
        if not osp.exists(self.dataset_dir):
            raise RuntimeError("'{}' is not available".format(self.dataset_dir))
        if not osp.exists(self.train_dir):
            raise RuntimeError("'{}' is not available".format(self.train_dir))
        if not osp.exists(self.query_dir):
            raise RuntimeError("'{}' is not available".format(self.query_dir))
        if not osp.exists(self.gallery_dir):
            raise RuntimeError("'{}' is not available".format(self.gallery_dir))

    def _process_dir(self, dir_path, relabel=False, training=False):

        img_paths = glob.glob(osp.join(dir_path, '*.jpg'))
        pattern = re.compile(r'([-\d]+)_([-\d]+)_c([-\d]+)_([-\d]+)')
        pid_container = set()
        for img_path in img_paths:
            pid, _, camid, clothid = map(int, pattern.search(img_path).groups())
            if pid == -1: continue  # junk images are just ignored
            pid_container.add(pid)

        pid2label = {pid: label for label, pid in enumerate(pid_container)}



        dataset = []
        for img_path in img_paths:
            img_prefix = img_path.split('.')
            img_path = img_prefix[0] + '.jpg'
            pid, _, camid, clothid = map(int, pattern.search(img_path).groups())

            if training:
                self.id_label_list.append(pid)
            if pid == -1: continue  # junk images are just ignored

            assert 0 <= pid <= 267
            assert 0 <= camid <= 12



            if relabel: pid = pid2label[pid]
            if training: assert 0 <= pid <= 133

            dataset.append((img_path, pid, clothid, camid,'CSCC'))

        return dataset


    def get_imagedata_info(self, data):
        pids, cams, clothids = [], [], []
        for img_path, pid, clothid,camid,datasetname in data:
            pids += [pid]
            cams += [camid]

        pids = set(pids)
        cams = set(cams)
        num_pids = len(pids)
        num_cams = len(cams)
        num_imgs = len(data)

        return num_pids, num_imgs, num_cams

    def print_dataset_statistics(self, train, query, gallery):
        num_train_pids, num_train_imgs, num_train_cams = self.get_imagedata_info(train)
        num_query_pids, num_query_imgs, num_query_cams = self.get_imagedata_info(query)
        num_gallery_pids, num_gallery_imgs, num_gallery_cams = self.get_imagedata_info(gallery)

        print("Dataset statistics:")
        print("  ----------------------------------------")
        print("  subset   | # ids | # images | # cameras |")
        print("  ----------------------------------------")
        print("  train    | {:5d} | {:8d} | {:9d}|".format(num_train_pids, num_train_imgs, num_train_cams))
        print("  query    | {:5d} | {:8d} | {:9d}|".format(num_query_pids, num_query_imgs, num_query_cams))
        print("  gallery  | {:5d} | {:8d} | {:9d}|".format(num_gallery_pids, num_gallery_imgs, num_gallery_cams))
        print("  ----------------------------------------")
