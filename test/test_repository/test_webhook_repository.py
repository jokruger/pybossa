# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2015 SciFabric LTD.
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.
# Cache global variables for timeouts

from default import Test, db
from nose.tools import assert_raises
from factories import TaskRunFactory
from pybossa.repositories import WebhookRepository
from pybossa.exc import WrongObjectError, DBIntegrityError
from pybossa.model.webhook import Webhook


class TestWebhookRepository(Test):

    payload = dict(foo='bar')

    def setUp(self):
        super(TestWebhookRepository, self).setUp()
        self.webhook_repo = WebhookRepository(db)
        TaskRunFactory.create()
        webhook = Webhook(project_id=1, payload=self.payload)
        self.webhook_repo.save(webhook)


    def test_get_return_none_if_no_webhook(self):
        """Test get method returns None if there is no log with the
        specified id."""

        assert self.webhook_repo.get(2) is None

    def test_get_return_obj(self):
        """Test get method returns obj."""

        tmp = self.webhook_repo.get(1)
        assert tmp.id == 1
        assert tmp.project_id == 1

    def test_get_by_return_obj(self):
        """Test get_by method returns obj."""

        tmp = self.webhook_repo.get_by(project_id=1)
        assert tmp.id == 1
        assert tmp.project_id == 1
