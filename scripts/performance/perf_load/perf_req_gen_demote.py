from indy import ledger
import json

from perf_load.perf_req_gen import RequestGenerator
from perf_load.perf_utils import PoolRegistry


class RGDemoteNode(RequestGenerator):
    _req_types = ["0"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pool_registry = PoolRegistry()

    def _rand_data(self):
        # pick random node from PoolRegistry to demote it
        result = self._pool_registry.select_new_random_node()
        return result

    async def _gen_req(self, submitter_did, req_data):
        data = {
            'alias': req_data['node_alias'],
            'services': []
        }
        return await ledger.build_node_request(submitter_did, req_data['node_dest'], json.dumps(data))
