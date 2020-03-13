/** @jsx jsx */

import * as React from 'react';
import { jsx } from '@emotion/core';
import { useQuery } from '@apollo/react-hooks';
import { useRouter } from 'next/router';

import { STAT_GROUPS, mq } from 'common/constants';
import ItemSelector from './ItemSelector';
import Layout from './Layout';
import StatTable from './StatTable';
import { ResponsiveGrid } from 'common/wrappers';

import {
  customSet,
  customSetVariables,
} from 'graphql/queries/__generated__/customSet';
import CustomSetQuery from 'graphql/queries/customSet.graphql';
import { getStatsFromCustomSet } from 'common/utils';
import SetHeader from './SetHeader';
import EquipmentSlots from './EquipmentSlots';
import { itemSlots_itemSlots } from 'graphql/queries/__generated__/itemSlots';

const SetBuilder: React.FC = () => {
  const router = useRouter();
  const { id: setId } = router.query;

  const { data: customSetData } = useQuery<customSet, customSetVariables>(
    CustomSetQuery,
    { variables: { id: setId }, skip: !setId },
  );

  const [
    selectedItemSlot,
    selectItemSlot,
  ] = React.useState<itemSlots_itemSlots | null>(null);

  React.useEffect(() => {
    function onKeyDown(e: KeyboardEvent) {
      if (e.keyCode === 27) {
        selectItemSlot(null);
      }
    }
    if (document) {
      document.addEventListener('keydown', onKeyDown);
    }
    return () => document && document.removeEventListener('keydown', onKeyDown);
  }, []);

  const statsFromCustomSet = React.useMemo(
    () => getStatsFromCustomSet(customSetData?.customSetById),
    [customSetData],
  );

  return (
    <Layout>
      <SetHeader customSet={customSetData?.customSetById} />
      <EquipmentSlots
        customSet={customSetData?.customSetById}
        selectItemSlot={selectItemSlot}
        selectedItemSlotId={selectedItemSlot?.id ?? null}
      />
      <div
        css={{
          flex: '1 1 auto',
          overflowX: 'hidden',
          paddingLeft: 20,
          display: 'flex',
        }}
      >
        <div css={{ flex: '0 1 584px', overflow: 'auto', marginTop: 12 }}>
          <ResponsiveGrid
            numColumns={[2, 2, 2, 2, 2, 2]}
            css={{ marginBottom: 20 }}
          >
            {STAT_GROUPS.map((group, idx) => (
              <StatTable
                key={idx}
                group={group}
                statsFromCustomSet={statsFromCustomSet}
                customSet={customSetData?.customSetById}
              />
            ))}
          </ResponsiveGrid>
        </div>
        <div
          css={{
            display: 'none',
            marginTop: 12,
            padding: '0 20px',
            [mq[1]]: {
              display: 'block',
              flex: 1,
            },
            overflow: 'auto',
          }}
        >
          <ItemSelector
            key={`selected-item-slot-${selectedItemSlot?.id}`}
            selectedItemSlot={selectedItemSlot}
            customSet={customSetData?.customSetById}
          />
        </div>
      </div>
    </Layout>
  );
};

export default SetBuilder;
